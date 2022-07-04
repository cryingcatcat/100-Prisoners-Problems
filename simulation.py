import random

class Simulation:
    def loop_constraint(self, box, i):
        temp = []
        initial_index = i
        while True:
            if box[i] == initial_index: #if current element is the same as the initial index, it means we formed a loop.
                temp.append(box[i])
                break
            else:                       #restore the current element & allocate new index.
                temp.append(box[i])
                i = box[i]
        return temp

    def begin_simulation(self):
        box = random.sample(range(100), 100)
        all_loops = []
        used = {}
        for i in range(len(box)):
            if box[i] not in used:      #check if current element has appeared in existed loops.
                all_loops.append(self.loop_constraint(box, i))
                for j in all_loops[-1]:
                    used[j] = 1

        for each in all_loops:  #if any loop has a length greater than 50, it means we have failed.
            if len(each) > 50:
                return False
        return True

    def get_rate(self): #simulate up to 1000 times.
        success = 0
        fail = 0
        for i in range(1000):
            if self.begin_simulation():
                success += 1
            else:
                fail += 1
        return success/(1000)
