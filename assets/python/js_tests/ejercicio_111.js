module.exports = {
    id: 111,
    nombreFuncion: 'tieneSubconjuntoSuma',
    descripcion: 'Implementa una función llamada "tieneSubconjuntoSuma" que determine si un array de números "numeros" tiene un subconjunto que sume exactamente "objetivo".',
    casos: [
      { input: [[3, 34, 4, 12, 5, 2], 9], expected: true },
      { input: [[3, 34, 4, 12, 5, 2], 30], expected: false },
      { input: [[1, 2, 3, 4], 5], expected: true }
    ]
  };