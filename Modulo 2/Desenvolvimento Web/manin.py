import requests

dados ={
    'Heloisa':'Meu post',
    'Email':'Heloisa@gmail.com'
}


response = requests.get('http://172.25.253.124:5000/alunos')
enviar = requests.post('http://172.25.253.124:5000/alunos',json=dados)

if response.status_code == 200:
  print("Requisição bem-sucedida!")
  print(response.json())
else:
  print(f"Erro na requsição. Código de status: {response.status_code}")
enviar.json()