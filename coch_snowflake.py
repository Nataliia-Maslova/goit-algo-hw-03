import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_snowflake(t, order-1, size)
        t.left(60)
        koch_snowflake(t, order-1, size)
        t.right(120)
        koch_snowflake(t, order-1, size)
        t.left(60)
        koch_snowflake(t, order-1, size)

def main():
    screen = turtle.Screen()
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)

    # Запит рівня рекурсії у користувача
    order = int(input("Введіть рівень рекурсії: "))
    size = 300

    # Малювання сніжинки Коха
    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

    screen.mainloop()

if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()