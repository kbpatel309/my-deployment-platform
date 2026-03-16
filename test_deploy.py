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

    # Install Dependencies
    print(f"Installing Dependencies")
    os.chdir(f'deployments/{project_name}')

    # Use --legacy-peer-deps to handle dependency conflicts
    os.system('npm install --legacy-peer-deps')

    print(f"Dependencies installed")

    # New: Build the project
    print(f"Building project")
    result = os.system("npm run build")

    if result == 0:
        print(f"Build complete!")
        print(f"Deployment finished!")
    else:
        print(f"Build failed!")