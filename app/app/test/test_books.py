def test_index(client):
    # Enviar una solicitud GET a la ruta index
    response = client.get('/Book/')
    
    # Verificar que la petición fue exitosa
    assert response.status_code == 200
    assert b"Libros" in response.data  # Asumiendo que hay un texto "Libros" en la página

def test_add_book(client, author):
    # Enviar una solicitud POST con los datos del nuevo libro
    response = client.post('/Book/add', data={
        'titleBook': 'new_book',
        'authorId': author.idAuthor
    }, follow_redirects=True)
    
    # Verificar que la operación fue exitosa
    assert response.status_code == 200
    assert b"new_book" in response.data  # Asumiendo que el título del libro se muestra en la página

def test_edit_book(client, book, author):
    # Enviar una solicitud POST para actualizar un libro existente
    response = client.post(f'/Book/edit/{book.idBook}', data={
        'titleBook': 'updated_book',
        'authorId': author.idAuthor
    }, follow_redirects=True)
    
    # Verificar que la actualización fue exitosa
    assert response.status_code == 200
    assert b"updated_book" in response.data  # Asumiendo que el título actualizado se muestra en la página

def test_delete_book(client, book):
    # Enviar una solicitud GET para eliminar el libro
    response = client.get(f'/Book/delete/{book.idBook}', follow_redirects=True)
    
    # Verificar que la eliminación fue exitosa
    assert response.status_code == 200
    assert b"Libros" in response.data  # Asumiendo que redirige correctamente
