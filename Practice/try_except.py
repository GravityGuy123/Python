def demo_try_except():
    try:
        # 1. ZeroDivisionError
        print("Division:", 10 / 0)

        # 2. ValueError
        num = int("abc")

        # 3. IndexError
        my_list = [1, 2, 3]
        print(my_list[5])

        # 4. KeyError
        my_dict = {"a": 1, "b": 2}
        print(my_dict["c"])

        # 5. TypeError
        result = "5" + 10

        # 6. FileNotFoundError
        with open("not_a_real_file.txt", "r") as f:
            content = f.read()

        # 7. AttributeError
        x = 5
        x.append(10)  # integers don't have append()

        # 8. ImportError
        import not_a_real_module

    except ZeroDivisionError as e:
        print("❌ Cannot divide by zero:", e)

    except ValueError as e:
        print("❌ Invalid value:", e)

    except IndexError as e:
        print("❌ List index out of range:", e)

    except KeyError as e:
        print("❌ Dictionary key not found:", e)

    except TypeError as e:
        print("❌ Wrong data type:", e)

    except FileNotFoundError as e:
        print("❌ File not found:", e)

    except AttributeError as e:
        print("❌ Attribute does not exist:", e)

    except ImportError as e:
        print("❌ Import error:", e)

    except Exception as e:
        print("❌ General error:", e)

    finally:
        print("✅ Done checking common exceptions!")


# Run the demo
demo_try_except()