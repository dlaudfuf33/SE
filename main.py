# main.py

from plot_utils import generate_data, create_plots

def main():
    variable_1, variable_2 = generate_data()
    create_plots(variable_1, variable_2)

if __name__ == "__main__":
    main()
