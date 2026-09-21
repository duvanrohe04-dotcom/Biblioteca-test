def test_index(client):
    # Enviar una solicitud GET a la ruta index
    response = client.get('/Loan/')
    
    # Verificar que la petición fue exitosa
    assert response.status_code == 200
    assert b"Prestamos" in response.data  # Asumiendo que hay un texto "Prestamos" en la página

def test_add_loan(client, user, book):
    # Enviar una solicitud POST con los datos del nuevo préstamo
    response = client.post('/Loan/add', data={
        'userId': user.idUser,
        'bookId': book.idBook
    }, follow_redirects=True)
    
    # Verificar que la operación fue exitosa
    assert response.status_code == 200
    assert b"Prestamos" in response.data  # Asumiendo que redirige y muestra los préstamos

def test_edit_loan(client, loan):
    # Enviar una solicitud POST para actualizar un préstamo existente
    response = client.post(f'/Loan/edit/{loan.idLoan}', data={
        'returnDate': '2023-12-31',
        'fine': '10.0',
        'status': 'Returned'
    }, follow_redirects=True)
    
    # Verificar que la actualización fue exitosa
    assert response.status_code == 200
    assert b"Returned" in response.data  # Asumiendo que el estado actualizado se muestra en la página

def test_delete_loan(client, loan):
    # Enviar una solicitud GET para eliminar el préstamo
    response = client.get(f'/Loan/delete/{loan.idLoan}', follow_redirects=True)
    
    # Verificar que la eliminación fue exitosa
    assert response.status_code == 200
    assert b"Prestamos" in response.data  # Asumiendo que redirige correctamente

def test_return_loan(client, loan):
    # Enviar una solicitud GET para procesar la devolución de un préstamo
    response = client.get(f'/Loan/return/{loan.idLoan}', follow_redirects=True)
    
    # Verificar que la devolución fue exitosa
    assert response.status_code == 200
    assert b"Returned" in response.data  # Asumiendo que el estado actualizado a Returned se muestra
