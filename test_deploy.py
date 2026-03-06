import os

def deploy_site(github_url, project_name):
    print(f"Cloning {github_url}")
    # check if path doesn't exist
    if not os.path.exists('deployments'):
        os.makedirs('deployments')
    
    # Clone the repo
    clone_command = f"git clone {github_url} deployments/{project_name}"
    os.system(clone_command)
    print(f"Cloned!")