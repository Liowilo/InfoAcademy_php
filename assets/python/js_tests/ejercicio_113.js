module.exports = {
    id: 113,
    nombreFuncion: 'ordenarPorFrecuencia',
    descripcion: 'Implementa una función llamada "ordenarPorFrecuencia" que ordene un array de números "numeros" por su frecuencia de aparición, de mayor a menor.',
    casos: [
      { input: [2,3,2,4,5,12,2,3,3,3,12], expected: [3,3,3,3,2,2,2,12,12,4,5] },
      { input: [1,1,2,2,3], expected: [1,1,2,2,3] },
      { input: [1,2,3,4,5], expected: [5,4,3,2,1] }
    ]
  };