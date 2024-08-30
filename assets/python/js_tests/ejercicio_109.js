module.exports = {
    id: 109,
    nombreFuncion: 'sonAnagramas',
    descripcion: 'Escribe una función llamada "sonAnagramas" que tome dos cadenas "str1" y "str2" y determine si son anagramas.',
    casos: [
      { input: ['listen', 'silent'], expected: true },
      { input: ['hello', 'world'], expected: false },
      { input: ['Debit Card', 'Bad Credit'], expected: true }
    ]
  };