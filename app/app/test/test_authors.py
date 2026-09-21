def test_index(client):
    # Enviar una solicitud GET a la ruta index
    response = client.get('/Author/')
    
    # Verificar que la petición fue exitosa
    assert response.status_code == 200
    assert b"Autores" in response.data  # Asumiendo que hay un texto "Autores" en la página

def test_add_author(client):
    # Enviar una solicitud POST con los datos del nuevo autor
    response = client.post('/Author/add', data={
        'nameAuthor': 'new_author',
        'nationalityAuthor': 'new_nationality'
    }, follow_redirects=True)
    
    # Verificar que la operación fue exitosa y se redirigió correctamente
    assert response.status_code == 200
    assert b"new_author" in response.data  # Asumiendo que el nombre del autor se muestra en la página

def test_edit_author(client, author):
    # Enviar una solicitud POST para actualizar un autor existente
    response = client.post(f'/Author/edit/{author.idAuthor}', data={
        'nameAuthor': 'updated_author',
        'nationalityAuthor': 'updated_nationality'
    }, follow_redirects=True)
    
    # Verificar que la actualización fue exitosa
    assert response.status_code == 200
    assert b"updated_author" in response.data  # Asumiendo que el nombre actualizado se muestra en la página

def test_delete_author(client, author):
    # Enviar una solicitud GET para eliminar el autor
    response = client.get(f'/Author/delete/{author.idAuthor}', follow_redirects=True)
    
    # Verificar que la eliminación fue exitosa
    assert response.status_code == 200
    assert b"Autores" in response.data  # Asumiendo que hay un mensaje de confirmación o redirección a la lista
