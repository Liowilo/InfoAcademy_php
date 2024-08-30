module.exports = {
    id: 110,
    nombreFuncion: 'esPalindromo',
    descripcion: 'Crea una función llamada "esPalindromo" que verifique si una cadena "texto" es un palíndromo, ignorando espacios y signos de puntuación.',
    casos: [
      { input: 'Anita lava la tina', expected: true },
      { input: 'Hola mundo', expected: false },
      { input: 'A man, a plan, a canal: Panama', expected: true }
    ]
  };