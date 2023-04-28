import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    best_fitness = 0
    # xác định dân số ban đầu của quần thể
    population_size = 20
    # xác định số thế hệ (lần lặp lại) thuật toán
    num_generations = 0
    # Tỉ lệ đột biến
    mutation_rate = 10
    # Số lượng chọn cá thể ưu tú để bỏ vào quần thể mới
    num_elite_schedule = 1

    # Tạo quần thể ban đầu
    population = Population(population_size)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    best_fitness = population.get_schedules()[0].get_fitness()
    # Khởi tạo và chạy thuật toán GA
    ga = GA()
    start_time = time.time()

    while(float(best_fitness) != 1.000):
        num_generations += 1
        print('Số thế hệ: ', num_generations)
        population = ga.run(population,mutation_rate,num_elite_schedule)    
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        best_fitness = population.get_schedules()[0].get_fitness()
        print('Số lượng schedule trong quần thể: ', len(population.get_schedules()))
        print('Best schedule fitness: ', best_fitness)

    end_time = time.time()
    print("Thời gian chạy thuật toán: ", end_time - start_time, " giây")
    print('Best schedule fitness: ', best_fitness)
    display.print_schedule(population.get_schedules()[0])

if __name__ == "__main__":
    main()