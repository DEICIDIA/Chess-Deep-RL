function onChange (oldPos, newPos) {
  console.log('Position changed:')
  console.log('Old position: ' + Chessboard.objToFen(oldPos))
  console.log('New position: ' + Chessboard.objToFen(newPos))
  console.log('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
}

var config = {
  draggable: true,
  position: 'start',
  onChange: onChange
}
var board = Chessboard('myBoard', config)

$('#ruyLopezBtn').on('click', function () {
  var ruyLopez = 'r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R'
  board.position(ruyLopez)
})

$('#startPositionBtn').on('click', board.start)