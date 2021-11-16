# story.py
import context as c


def menu1(ctx):
    prompt = "oh damn a dog"
    options = []
    options.append(c.create_menu_item(1, "what da dog doin", menu1_a))
    options.append(c.create_menu_item(2, "how da dog doin", menu1_b))
    options.append(c.create_menu_item(3, "shoot it", menu1_c))
    options.append(c.create_menu_item(4, "exit", None))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def menu1_a(ctx):
    prompt = "your mom lol"
    options = []
    options.append(c.create_menu_item(1, "return", menu1))
    options.append(c.create_menu_item(2, "what da dog doin doe", menu1_a))
    options.append(c.create_menu_item(3, "but how da dog doin", menu1_b))
    options.append(c.create_menu_item(4, "bro thats it ima shoot it", menu1_c))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def menu1_b(ctx):
    prompt = """da dog got divorced, children died in car accident with mother
                father got cancer, owner disowned him, canceled on twitter
                blocked by every meme account on insta, also he got a 2 in ib physics
            """
    options = []
    options.append(c.create_menu_item(1, "ok but who asked", menu1_a))
    options.append(c.create_menu_item(2, "ima put this dog out of his misery", menu1_c))
    options.append(
        c.create_menu_item(3, "you know what, ima take care of him", menu1_d)
    )
    options.append(c.create_menu_item(4, "quit", None))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def menu1_c(ctx):
    prompt = "you made a big mistake, its not a dog, its a dawg"
    options = []
    options.append(c.create_menu_item(1, "oh shit what the dawg doin", menu1_a))
    options.append(c.create_menu_item(2, "oh shit aight how do daw doin den", menu1_b))
    options.append(
        c.create_menu_item(3, "just a prank bro ima take u to the vet", menu1_d)
    )
    options.append(c.create_menu_item(4, "exit", None))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def menu1_d(ctx):
    prompt = "cant afford the medical bill, doctor please euthanize him"
    options = []
    options.append(c.create_menu_item(1, "bruh(who your financial support)", menu1_a))
    options.append(c.create_menu_item(2, "bruh(how da dawg doin)", menu1_b))
    options.append(c.create_menu_item(3, "bruh(whats a dog?)", menu1_c))
    options.append(c.create_menu_item(4, "exit", None))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def main():
    ctx = c.init()
    cb = menu1(ctx)
    while cb != None:
        cb = cb(ctx)


if __name__ == "__main__":
    main()
