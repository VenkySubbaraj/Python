import requests

def fetch_artifacts(source_repo_url, source_repo_user, source_repo_pass):
    url = f"{source_repo_url}/service/rest/v1/components"
    response = requests.get(url, auth=(source_repo_user, source_repo_pass))

    if response.status_code == 200:
        data = response.json()
        artifacts = data['items']
        return artifacts
    else:
        print(f"Error fetching artifacts: {response.status_code}")
        return []

def copy_artifacts(artifacts, destination_repo_url, destination_repo_user, destination_repo_pass):
    for artifact in artifacts:
        artifact_id = artifact['id']
        artifact_url = artifact['assets'][0]['downloadUrl']

        response = requests.get(artifact_url, stream=True)
        if response.status_code == 200:
            artifact_data = response.content
            upload_url = f"{destination_repo_url}/service/rest/v1/components"
            upload_response = requests.post(upload_url, auth=(destination_repo_user, destination_repo_pass), data=artifact_data)
            if upload_response.status_code == 201:
                print(f"Artifact {artifact_id} copied successfully.")
            else:
                print(f"Error copying artifact {artifact_id}: {upload_response.status_code}")
        else:
            print(f"Error downloading artifact {artifact_id}: {response.status_code}")

if __name__ == "__main__":
    source_repo_url = "SOURCE_REPOSITORY_URL"
    source_repo_user = "SOURCE_USERNAME"
    source_repo_pass = "SOURCE_PASSWORD"

    destination_repo_url = "DESTINATION_REPOSITORY_URL"
    destination_repo_user = "DESTINATION_USERNAME"
    destination_repo_pass = "DESTINATION_PASSWORD"

    artifacts = fetch_artifacts(source_repo_url, source_repo_user, source_repo_pass)
    copy_artifacts(artifacts, destination_repo_url, destination_repo_user, destination_repo_pass)
