from Scene import Scene
class Agent:
    def __init__(self, scene):
        self.scene = Scene()
        self.id = self.scene.get_id()
        #Это херня, у нас получается у каждого агента свой экземпляр сцены 
        #И у всех нулевой id

