class Scene:
    def __init__(self):
        self.ids = [0, []]

    def get_scene(self, agent):
        return self

    def get_id(self, agent):
        agent.id = self.ids[0]
        self.ids[0]+=1
        self.ids[1].append(agent)
