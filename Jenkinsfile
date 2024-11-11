pipeline {
    agent any
    
    parameters {
        choice(
            name: 'Opcion',
            choices: ['Trivia', 'Procesar Pedidos', 'Consultas USQL'],
            description: '---------- Elige una opción para ejecutar -------------'
        )
    }

    
    stages {
        stage('Selección de Opción') {
            steps {
                script {
                    echo "--------------------------------------"
                    echo "Opción seleccionada: ${params.Opcion}"
                    echo "--------------------------------------"
                }
            }
        }

        stage('Instalar Dependencias') {
            steps {
                dir('Entregable1') {
                    bat 'python -m pip install -r requirements.txt'
                }
            }
        }

        stage('Ejecutar Opción Seleccionada') {
            steps {
                script {
                    if (params.Opcion == 'Trivia') {
                        
                        echo "--------------------------------------"
                        echo 'Ejecutando el juego de Trivia...I1'
                        echo "--------------------------------------"
                        
                        // Acá se ejecuta el código correspondiente al trivia
                        
                        dir('Entregable1') {
                            bat 'python Principal.py'
                        }
                        
                    } else if (params.Opcion == 'Procesar Pedidos') {
                        
                        echo "--------------------------------------"
                        echo 'Procesando pedidos...'
                        echo "--------------------------------------"
                        
                        // Acá se ejecuta el código correspondiente al procesamiento de pedidos
                        
                        // sh 'git clone https://github.com/tu_usuario/entregable2_pedidos.git'
                        // sh 'python entregable2_pedidos/main.py'
                        
                    } else if (params.Opcion == 'Consultas USQL') {
                        
                        echo "--------------------------------------"
                        echo 'Ejecutando consultas USQL...'
                        echo "--------------------------------------"
                        
                        // Acá se ejecuta el código correspondiente a las consultas USQL
                        
                        // sh 'git clone https://github.com/tu_usuario/entregable3_usql.git'
                        // sh 'python entregable3_usql/main.py'
                    }
                }
            }
        }
    }
    
    post {
        success {
            echo "--------------------------------------"
            echo 'Pipeline completado con éxito.'
            echo "--------------------------------------"
        }
        failure {
            echo "--------------------------------------"
            echo 'Hubo un error en el pipeline.'
            echo "--------------------------------------"
        }
    }
}