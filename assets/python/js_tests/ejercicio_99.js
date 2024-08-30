module.exports = {
    id: 99,
    nombreFuncion: 'saludar',
    descripcion: 'Crea una función llamada "saludar" que tome un parámetro "nombre" y devuelva un saludo personalizado. Ejemplo: "Hola, {nombre}!"',
    casos: [
      { input: 'María', expected: 'Hola, María!' },
      { input: 'Juan', expected: 'Hola, Juan!' },
      { input: '', expected: 'Hola, !' }
    ]
  };