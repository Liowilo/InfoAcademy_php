module.exports = {
    id: 112,
    nombreFuncion: 'esArbolBalanceado',
    descripcion: 'Crea una función llamada "esArbolBalanceado" que determine si un árbol binario está balanceado. La función debe recibir el nodo raíz del árbol.',
    casos: [
      { input: {valor: 1, izquierda: {valor: 2}, derecha: {valor: 3}}, expected: true },
      { input: {valor: 1, izquierda: {valor: 2, izquierda: {valor: 4}}}, expected: false },
      { input: null, expected: true }
    ]
  };