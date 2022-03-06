pipeline {

    agent any

    triggers {
        pollSCM 'H/15 * * * *'
    }

    options {
        timestamps()
        timeout(time: 600, unit: 'MINUTES')
        buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '30', numToKeepStr: ''))
        disableConcurrentBuilds()
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
                    bat 'docker-compose up -d'
                    }
                }
            }

        /* stage("Copy file to shared volume") {
            steps {
                script {
                    bat 'cp C:\\Users\\ziv\\.jenkins\\workspace\\flask-pipeline\\Resources\\scores.txt'
                    }
                }
            } */

		stage("Test application - e2e") {
            steps {
                script {
                    bat 'python e2e.py'
                    }
                }
            }

		stage("Terminate and push image") {
            steps {
                script {
                    bat 'docker-compose stop'
                    bat 'docker tag flask-image zivgadri/flask-image:latest'
                    bat 'docker push zivgadri/flask-image:latest'
                    }
                }
            }
        }
}