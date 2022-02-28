pipeline {

    parameters {
        choice(name: 'User_To_Check', choices: "Ziv\nRotem\nDanielle\nRaz", description: "choose the user you with to check for score")
    }

    agent any

    stages {

        stage("Checkout From SCM") {
            steps {
                script {
                    checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'WOG_FLASK', url: 'https://github.com/ZivGadriDevOps/WorldOfGames.git']]])
                    }
                }
            }
				stage("Build a docker image") {
            steps {
                script {
                    bat 'sudo docker build -t flask-image .'
                    }
                }
            }
				stage("Run docker image") {
            steps {
                script {
                    bat 'sudo docker run -d -p 8777:5000 flask-image .'
                    }
                }
            }
				stage("Test application - e2e") {
            steps {
                script {
                    bat 'python Tests/e2e.py'
                    }
                }
            }
				stage("Terminate and push image") {
            steps {
                script {
                    bat 'sudo docker run -d -p 8777:5000 flask-image .'
                    }
                }
            }
        }
}