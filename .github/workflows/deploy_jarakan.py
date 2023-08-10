name: Deploy Jarakan

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest
    environment: gcp_minimum
    steps:
    - uses: actions/checkout@v1

    - name: SSH Using Appleboy
      uses: appleboy/ssh-action@master
      env:
        HOST: ${{ secrets.HOST_JARAKAN }}
        USERNAME: ${{ secrets.USERNAME }}
        PORT: 22
        PASSWORD: ${{ secrets.PASSWORD }}
      with:
        envs: HOST, USERNAME, PASSWORD
        host: ${{ secrets.HOST_JARAKAN }}
        username: ${{ secrets.USERNAME }}
        port: 22
        password: ${{ secrets.PASSWORD }}
        script: cd "/home/${USERNAME}/Web-KKN" && git add . && git stash && git pull origin main && python3 deploy.py