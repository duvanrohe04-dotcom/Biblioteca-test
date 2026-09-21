def test_index(client):
    # Enviar una solicitud GET a la ruta index
    response = client.get('/room/')
    
    # Verificar que la petición fue exitosa
    assert response.status_code == 200
    assert b"Salas" in response.data  # Asumiendo que hay un texto "Salas" en la página

def test_add_room(client):
    # Enviar una solicitud POST con los datos de la nueva sala
    response = client.post('/room/add', data={
        'name': 'new_room',
        'description': 'new_description'
    }, follow_redirects=True)
    
    # Verificar que la operación fue exitosa
    assert response.status_code == 200
    assert b"new_room" in response.data  # Asumiendo que el nombre de la sala se muestra en la página

def test_edit_room(client, room):
    # Enviar una solicitud POST para actualizar una sala existente
    response = client.post(f'/room/edit/{room.id}', data={
        'name': 'updated_room',
        'description': 'updated_description'
    }, follow_redirects=True)
    
    # Verificar que la actualización fue exitosa
    assert response.status_code == 200
    assert b"updated_room" in response.data  # Asumiendo que el nombre actualizado se muestra en la página

def test_delete_room(client, room):
    # Enviar una solicitud GET para eliminar la sala
    response = client.get(f'/room/delete/{room.id}', follow_redirects=True)
    
    # Verificar que la eliminación fue exitosa
    assert response.status_code == 200
    assert b"Salas" in response.data  # Asumiendo que redirige correctamente
