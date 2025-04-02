pipeline{
    agent any
    stages{
        stage('check python version'){
         steps{
           bat 'python --version'
        }   
        }
stage(Adding git credentials){
steps{
checkout([
                    branches: [[name: '*/master']], // Replace 'main' with your branch name
                    userRemoteConfigs: [[url: 'https://github.com/MG1902/Testing-jenkins.git']]
                ])
}
}
        stage('Run Main.py')
        {
            steps
            {
                bat 'python Main.py'
            }
        }
    }
    
}
