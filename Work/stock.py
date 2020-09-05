class Stock:
  __slots__ = ('name','_shares', 'price')
  def __init__(self, name, shares, price):

    self._shares = shares
    
    self.name = name    
    self.price = price
  
  def __repr__(self):
    return f'Stock({self.name},{self.shares},{self.price})'
  
  @property
  def cost(self):
    return self.shares * self.price
    
  def sell(self, num_shares):
    self.shares -= num_shares
    return
  
  @property
  def shares(self):
    return self._shares
  
  @shares.setter
  def shares(self, value):
    if not isinstance(value, int):
      raise TypeError('Expected int')
    self._shares = value
