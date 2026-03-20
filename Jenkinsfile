pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-app"
        VM_MASTER  = "192.168.64.2"
        VM_NODE1   = "192.168.64.3"
        VM_NODE2   = "192.168.64.4"
    }

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Bertrussoff/devops-flask-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:latest .'
            }
        }
        stage('Trivy Scan') {
            steps {
                sh 'trivy image --exit-code 0 --severity HIGH,CRITICAL ${IMAGE_NAME}:latest'
            }
        }
        stage('Deploy to vm-master') {
            steps {
                sh '''
                    docker stop ${IMAGE_NAME} || true
                    docker rm ${IMAGE_NAME} || true
                    docker run -d --name ${IMAGE_NAME} -p 5000:5000 ${IMAGE_NAME}:latest
                '''
            }
        }
        stage('Deploy to vm-node1') {
            steps {
                sh '''
                    docker save ${IMAGE_NAME}:latest | ssh bert@${VM_NODE1} "docker load"
                    ssh bert@${VM_NODE1} "docker stop ${IMAGE_NAME} || true"
                    ssh bert@${VM_NODE1} "docker rm ${IMAGE_NAME} || true"
                    ssh bert@${VM_NODE1} "docker run -d --name ${IMAGE_NAME} -p 5000:5000 ${IMAGE_NAME}:latest"
                '''
            }
        }
        stage('Deploy to vm-node2') {
            steps {
                sh '''
                    docker save ${IMAGE_NAME}:latest | ssh bert@${VM_NODE2} "docker load"
                    ssh bert@${VM_NODE2} "docker stop ${IMAGE_NAME} || true"
                    ssh bert@${VM_NODE2} "docker rm ${IMAGE_NAME} || true"
                    ssh bert@${VM_NODE2} "docker run -d --name ${IMAGE_NAME} -p 5000:5000 ${IMAGE_NAME}:latest"
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment successful on all 3 VMs! 🚀'
        }
        failure {
            echo 'Deployment failed! Check the logs.'
        }
    }
}
