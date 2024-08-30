module.exports = {
    id: 107,
    nombreFuncion: 'filtrarPares',
    descripcion: 'Crea una función llamada "filtrarPares" que tome un array de números "numeros" y devuelva un nuevo array solo con los números pares.',
    casos: [
      { input: [1,2,3,4,5,6], expected: [2,4,6] },
      { input: [1,3,5], expected: [] },
      { input: [2,4,6], expected: [2,4,6] }
    ]
  };