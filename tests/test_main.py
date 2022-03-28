import pytest
from fastapi.datastructures import UploadFile
from web.data.datamap import Datamap, DatamapLine
from web.exceptions import BadCSVError
from web.services.datamap_service import (
    get_datamaps,
    import_csv_to_datamap,
    get_datamap_by_id,
    get_datamap_lines_for_datamap,
    import_uploaded_csv_to_datamap,
    check_csv,
)


def test_index(client):
    response = client.get("/")
    assert response.url == "http://testserver/"
    assert response.status_code == 200


def test_projects_list_view(client, projects):
    response = client.get("/projects")
    assert "Boring Project" in response.text
    assert response.url == "http://testserver/projects"


def test_datamap_in_db(session, datamap):
    session = session()
    dm = session.query(Datamap).first()
    # TODO: this doesn't test our API
    assert dm.name == "Test Datamap"


def test_datamap_service(datamap):
    dms = get_datamaps()
    assert dms[0].name == "Test Datamap"  # type: ignore


def test_get_datamap_by_id(datamap):
    assert get_datamap_by_id(1).name == "Test Datamap"  # type: ignore


def test_get_datamap_lines_for_datamap(datamap, datamaplines):
    dmls = get_datamap_lines_for_datamap(datamap)
    assert dmls[0].datamap.id == datamap.id


def test_import_csv_lines_to_datamap(dm_csv, datamaplines, datamap, session):
    import_csv_to_datamap(dm_csv, datamap)
    session = session()
    dm = session.query(Datamap).first()
    assert dm.lines[-1].key == "Test Key from CSV 2"


def test_import_upload_datmap_csv(dm_csv, datamap, session):
    with open(dm_csv, "rb") as f:
        uf = UploadFile("toss.csv", f, "text/csv")
        import_uploaded_csv_to_datamap(uf, datamap.name)
        session = session()
        dml = session.query(DatamapLine).first()
        assert dml.key == "Test Key from CSV 1"


def test_check_valid_datamap_file(dm_csv):
    with open(dm_csv, "rb") as f:
        uf = UploadFile("toss.csv", f, "text/csv")
        assert check_csv(uf)


def test_check_invalid_datamap_file_key(dm_csv_bad_key):
    with open(dm_csv_bad_key, "rb") as f:
        uf = UploadFile("toss.csv", f, "text/csv")
        with pytest.raises(BadCSVError) as exc_info:
            check_csv(uf)
        assert exc_info.value.args[0] == "key header is not correct."


def test_check_invalid_datamap_file_sheet(dm_csv_bad_sheet):
    with open(dm_csv_bad_sheet, "rb") as f:
        uf = UploadFile("toss.csv", f, "text/csv")
        with pytest.raises(BadCSVError) as exc_info:
            check_csv(uf)
        assert exc_info.value.args[0] == "sheet header is not correct."


def test_check_invalid_datamap_file_datatype(dm_csv_bad_datatype):
    with open(dm_csv_bad_datatype, "rb") as f:
        uf = UploadFile("toss.csv", f, "text/csv")
        with pytest.raises(BadCSVError) as exc_info:
            check_csv(uf)
        assert exc_info.value.args[0] == "datatype header is not correct."


def test_check_invalid_datamap_file_cellref(dm_csv_bad_cellref):
    with open(dm_csv_bad_cellref, "rb") as f:
        uf = UploadFile("toss.csv", f, "text/csv")
        with pytest.raises(BadCSVError) as exc_info:
            check_csv(uf)
        assert exc_info.value.args[0] == "cellref header is not correct."


def test_reject_non_csv_file(dm_non_csv, datamap):
    with open(dm_non_csv, "rb") as f:
        uf = UploadFile("toss.csv", f, "text/csv")
        with pytest.raises(BadCSVError) as exc_info:
            import_uploaded_csv_to_datamap(uf, datamap.name)
        assert (
            exc_info.value.args[0] == "key header is not correct."
        )  # no header so defeault to this
