def test_index(client):
    # Enviar una solicitud GET a la ruta index
    response = client.get('/cloans/')
    
    # Verificar que la petición fue exitosa
    assert response.status_code == 200
    assert b"Prestamos" in response.data  # Asumiendo que hay un texto "Prestamos" en la página

def test_add_cloan(client, user, computer):
    # Enviar una solicitud POST con los datos del nuevo préstamo de computadora
    response = client.post('/cloans/add', data={
        'userId': user.idUser,
        'computerId': computer.idComputer,
        'loanDate': '2023-01-01',
        'returnDate': '2023-01-10',
        'status': 'Active'
    }, follow_redirects=True)
    
    # Verificar que la operación fue exitosa
    assert response.status_code == 200
    assert b"Active" in response.data  # Asumiendo que el estado se muestra en la página

def test_edit_cloan(client, cloan, user, computer):
    # Enviar una solicitud POST para actualizar un préstamo de computadora existente
    response = client.post(f'/cloans/update/{cloan.idLoan}', data={
        'userId': user.idUser,
        'computerId': computer.idComputer,
        'loanDate': '2023-01-01',
        'returnDate': '2023-01-15',
        'status': 'Returned'
    }, follow_redirects=True)
    
    # Verificar que la actualización fue exitosa
    assert response.status_code == 200
    assert b"Returned" in response.data  # Asumiendo que el estado actualizado se muestra en la página

def test_delete_cloan(client, cloan):
    # Enviar una solicitud POST para eliminar el préstamo de computadora
    response = client.post(f'/cloans/delete/{cloan.idLoan}', follow_redirects=True)
    
    # Verificar que la eliminación fue exitosa
    assert response.status_code == 200
    assert b"Prestamos" in response.data  # Asumiendo que redirige correctamente

def test_return_cloan(client, cloan):
    # Enviar una solicitud POST para procesar la devolución de la computadora
    response = client.post(f'/cloans/return/{cloan.idLoan}', follow_redirects=True)
    
    # Verificar que la devolución fue exitosa
    assert response.status_code == 200
    assert b"Returned" in response.data  # Asumiendo que el estado actualizado a Returned se muestra
