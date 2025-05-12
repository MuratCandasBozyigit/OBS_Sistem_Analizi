import Frames

if __name__ == "__main__":
    from DB import init_database
    init_database()
    Frames.build_gui()  