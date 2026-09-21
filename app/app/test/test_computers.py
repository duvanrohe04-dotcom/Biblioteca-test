def test_index(client):
    # Enviar una solicitud GET a la ruta index
    response = client.get('/computers/')
    
    # Verificar que la petición fue exitosa
    assert response.status_code == 200
    assert b"Computadoras" in response.data  # Asumiendo que hay un texto "Computadoras" en la página

def test_add_computer(client):
    # Enviar una solicitud POST con los datos de la nueva computadora
    response = client.post('/computers/add', data={
        'brandComputer': 'new_brand',
        'modelComputer': 'new_model',
        'statusComputer': 'Active'
    }, follow_redirects=True)
    
    # Verificar que la operación fue exitosa
    assert response.status_code == 200
    assert b"new_brand" in response.data  # Asumiendo que la marca se muestra en la página

def test_edit_computer(client, computer):
    # Enviar una solicitud POST para actualizar una computadora existente
    response = client.post(f'/computers/update/{computer.idComputer}', data={
        'brandComputer': 'updated_brand',
        'modelComputer': 'updated_model',
        'statusComputer': 'Inactive'
    }, follow_redirects=True)
    
    # Verificar que la actualización fue exitosa
    assert response.status_code == 200
    assert b"updated_brand" in response.data  # Asumiendo que el campo actualizado se muestra en la página

def test_delete_computer(client, computer):
    # Enviar una solicitud POST para eliminar la computadora
    response = client.post(f'/computers/delete/{computer.idComputer}', follow_redirects=True)
    
    # Verificar que la eliminación fue exitosa
    assert response.status_code == 200
    assert b"Computadoras" in response.data  # Asumiendo que redirige correctamente
