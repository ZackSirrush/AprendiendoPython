from sistema_biblioteca.biblioteca import Biblioteca
from sistema_biblioteca.libro import Libro

biblioteca_nacional = Biblioteca('Biblioteca Nacional')
print(f'Bienvenidos al buscador de la {biblioteca_nacional.nombre}')

#Definir libros
libro1 = Libro('Cien años de soledad', 'Gabriel García Márquez', 'Ficción')
libro2 = Libro('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Comedia')
libro3 = Libro('El amor en los tiempos del cólera', 'Gabriel García Márquez', 'Ficción')
libro4 = Libro('Pedro Páramo', 'Juan Rulfo', 'Ficción')
libro5 = Libro('Pantaleón y las visitadores', 'Mario Vargas Llosa', 'Comedia')

#Agregar libros a biblioteca
biblioteca_nacional.agregar_libro(libro1)
biblioteca_nacional.agregar_libro(libro2)
biblioteca_nacional.agregar_libro(libro3)
biblioteca_nacional.agregar_libro(libro4)
biblioteca_nacional.agregar_libro(libro5)

#Buscar libros por autor
autor = 'Gabriel García Márquez'
print(f'\nLibros de {autor}')
biblioteca_nacional.buscar_libro_por_autor(autor)

#Buscar libros por género
genero = 'Ficción'
print(f'\nLibros de {genero}')
biblioteca_nacional.buscar_libro_por_genero(genero)

#Mostrar todos los libros
biblioteca_nacional.mostrar_todos_los_libros()