import threading


class DiningPhilosophers:

    def __init__(self):
        # 5 tenedores (locks)
        self.forks = [threading.Lock() for _ in range(5)]
        self.output = []
        self.lock = threading.Lock()  # proteger el output

    def wantsToEat(self, philosopher: int):

        left = philosopher
        right = (philosopher + 1) % 5

        # Estrategia para evitar deadlock
        if philosopher % 2 == 0:
            first, second = left, right
            first_id, second_id = 1, 2   # left, right
        else:
            first, second = right, left
            first_id, second_id = 2, 1   # right, left

        # tomar primer tenedor
        with self.forks[first]:
            self._log(philosopher, first_id, 1)  # pick

            # tomar segundo tenedor
            with self.forks[second]:
                self._log(philosopher, second_id, 1)  # pick

                # comer
                self._log(philosopher, 0, 3)

                # soltar segundo tenedor
                self._log(philosopher, second_id, 2)

            # soltar primer tenedor
            self._log(philosopher, first_id, 2)

    def _log(self, philosopher, fork, action):
        with self.lock:
            self.output.append([philosopher, fork, action])


# ─────────────────────────────
# FUNCIÓN DE PRUEBA (como LeetCode)
# ─────────────────────────────

def run_test(n):
    dp = DiningPhilosophers()

    def task(i):
        for _ in range(n):
            dp.wantsToEat(i)

    threads = []
    for i in range(5):
        t = threading.Thread(target=task, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return dp.output


# ─────────────────────────────
# MAIN
# ─────────────────────────────

if __name__ == "__main__":
    n = 1
    result = run_test(n)

    print(result)
