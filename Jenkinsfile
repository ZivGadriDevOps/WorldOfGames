pipeline {

    agent any

    triggers {
        pollSCM 'H/15 * * * *'
    }

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
                    bat 'docker build -t flask-image:latest .'
                    }
                }
            }
				stage("Run docker image") {
            steps {
                script {
                    bat 'docker-compose up'
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
                    bat 'docker run -d -p 8777:5000 flask-image .'
                    }
                }
            }
        }
}