import os

# change directory to test deployment
os.chdir("test-deployment")

# installing dependencies
os.system("npm run install")

# building project
os.system("npm run build")

# build complete
# starting server
os.system("npm run start")




