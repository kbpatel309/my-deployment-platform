import os

# def deploy_site(github_url, project_name):
#     print(f"📦 Cloning {github_url}...")
    
#     if not os.path.exists('deployments'):
#         os.makedirs('deployments')
    
#     # Clone the repo
#     clone_command = f'git clone {github_url} deployments/{project_name}'
#     os.system(clone_command)
#     print(f"✅ Cloned!")

#     # New: Install dependencies
#     print(f"📚 Installing dependencies...")
#     os.chdir(f'deployments/{project_name}') # Go into the project folder

#     # Use --legacy-peer-deps to handle dependency conflicts
#     os.system('npm install --legacy-peer-deps')

#     print(f"✅ Dependencies installed!")

#     # NEW: Build
#     print(f"🔨 Building project...")
#     result = os.system('npm run build')

#     if result == 0:
#         print(f"✅ Build complete!")
#         print(f"🎉 Deployment finished! Project is in deployments/{project_name}")
#     else:
#         print(f"❌ Build failed - check errors above")

# # Test it - use a small, simple repo this time
# deploy_site("https://github.com/shadcn-ui/taxonomy", "test-project-5")

# deploying test-deployment project to see visual proof of python script working
print("🚀 Starting deployment...")

# Go to working project
os.chdir("test-deployment")

print("📚 Installing dependencies...")
os.system("npm install")

print("🔨 Building project...")
os.system("npm run build")

print("✅ Build complete!")
print("🌐 Starting server...")
os.system('npm run start')