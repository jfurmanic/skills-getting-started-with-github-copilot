def test_unregister_removes_participant_from_activity(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )
    activities_response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
    assert email not in activities_response.json()[activity_name]["participants"]


def test_unregister_returns_404_when_activity_not_found(client):
    # Arrange
    missing_activity = "Robotics Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{missing_activity}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_404_when_participant_not_found(client):
    # Arrange
    activity_name = "Chess Club"
    missing_email = "not.registered@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": missing_email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in activity"
