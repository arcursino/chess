class ImpossibleMove(Exception):
    pass


class InvalidChessColor(Exception):
    pass


class Piece(object):
    def __init__(self, color):
        color = color.lower()

        if color not in ['white', 'black']:
            raise InvalidChessColor('That color should be "black" or "white".')

        self.__color = color
        self.__moved = False
        self.__y = '12345678'
        self.__x = 'abcdefgh'

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def color(self):
        return self.__color

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def moved(self):
        return self.__moved

    @moved.setter
    def moved(self, value):
        self.__moved = value


class Bishop(Piece):
    def move(self, _from, to):
        self.moved = True
        if abs(self.x.index(_from[0]) - self.x.index(to[0])) == abs(self.y.index(to[1]) - self.y.index(_from[1])):
            return to
        raise ImpossibleMove("Bishop can't move to %s" % to)


class Rook(Piece):
    def move(self, _from, to):
        self.moved = True
        horizontal = self.x.index(_from[0]) == self.x.index(to[0]) and self.y.index(_from[1]) != self.y.index(to[1])
        vertical = self.x.index(_from[0]) != self.x.index(to[0]) and self.y.index(_from[1]) == self.y.index(to[1])

        if horizontal or vertical:
            return to
        raise ImpossibleMove("Rook can't move to %s" % to)


class King(Piece):
    def move(self, _from, to):
        self.moved = True
        x_distance = abs(self.x.index(_from[0]) - self.x.index(to[0]))
        y_distance = abs(self.y.index(_from[1]) - self.y.index(to[1]))

        if x_distance in [0, 1] and y_distance in [0, 1] and x_distance + y_distance != 0:
            return to
        raise ImpossibleMove("King can't move to %s" % to)


class Queen(Piece):
    def move(self, _from, to):
        self.moved = True
        # move as a Rook {{
        horizontal = self.x.index(_from[0]) == self.x.index(to[0]) and self.y.index(_from[1]) != self.y.index(to[1])
        vertical = self.x.index(_from[0]) != self.x.index(to[0]) and self.y.index(_from[1]) == self.y.index(to[1])

        if horizontal or vertical:
            return to
        # }}

        # move as a Bishop {{
        if abs(self.x.index(_from[0]) - self.x.index(to[0])) == abs(self.y.index(to[1]) - self.y.index(_from[1])):
            return to
        # }}

        raise ImpossibleMove("Queen can't move to %s" % to)


class Pawn(Piece):
    def move(self, _from, to):
        self.moved = True
        if self.x.index(_from[0]) == self.x.index(to[0]) and abs(self.y.index(to[1]) - self.y.index(_from[1])) == 1:
            return to
        raise ImpossibleMove("Pawn can't move to %s" % to)


class Knight(Piece):
    def move(self, _from, to):
        self.moved = True
        x_distance = abs(self.x.index(_from[0]) - self.x.index(to[0]))
        y_distance = abs(self.y.index(_from[1]) - self.y.index(to[1]))

        if x_distance in [1, 2] and y_distance in [1, 2] and x_distance != y_distance:
            return to
        raise ImpossibleMove("Knight can't move to %s" % to)