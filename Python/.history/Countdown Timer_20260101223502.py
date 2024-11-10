# Python Project Idea – A countdown timer is a useful tool for keeping track of time. In this project, we will create a countdown timer using Python. We will first create a function to take   time in seconds and print it out in a formatted string. We will then use this function to create a countdown timer.

# The countdown timer will start at a given time and count down to zero. At each second, it will print out the remaining time. When the timer reaches zero, it will print out a message saying, “Time’s up!.” This project is a great way to learn about working with time in Python. It is also a useful tool that you can use in your projects.



# Python-ის პროექტის იდეა – დროის თვალყურის დევნების სასარგებლო ინსტრუმენტია უკუთვლის ტაიმერი. ამ პროექტში, Python-ის გამოყენებით შევქმნით უკუთვლის ტაიმერს. თავდაპირველად შევქმნით ფუნქციას, რომელიც დროს წამებში გამოთვლის და ფორმატირებულ სტრიქონში დაბეჭდავს. შემდეგ ამ ფუნქციას გამოვიყენებთ უკუთვლის ტაიმერის შესაქმნელად.

# უკუთვლის ტაიმერი ჩაირთვება მოცემულ დროს და ნულამდე დაითვლის. ყოველ წამს ის დაბეჭდავს დარჩენილ დროს. როდესაც ტაიმერი ნულს მიაღწევს, ის დაბეჭდავს შეტყობინებას: „დრო ამოიწურა!“. ეს პროექტი შესანიშნავი საშუალებაა Python-ში დროსთან მუშაობის შესასწავლად. ის ასევე სასარგებლო ინსტრუმენტია, რომლის გამოყენებაც შეგიძლიათ თქვენს პროექტებში.



import builtins
import types
import importlib.util
import pathlib
import pytest


def _load_module_from_path(path_str: str):
    """
    Helper to dynamically load the user's module from the given path string.
    This avoids issues with spaces in filenames, such as 'Countdown Timer.py'.
    """
    path = pathlib.Path(path_str)
    spec = importlib.util.spec_from_file_location("countdown_timer_module", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


@pytest.fixture(scope="module")
def countdown_module():
    # 
    # Arrange
    module_path = r"c:\Users\Iliailia12\Desktop\Pyton Projects\Countdown Timer.py"
    module = _load_module_from_path(module_path)
    if not hasattr(module, "time_in_seconds") or not isinstance(
        getattr(module, "time_in_seconds"), types.FunctionType
    ):
        raise AttributeError(
            "The module must define a function named 'time_in_seconds'."
        )

    return module


@pytest.mark.parametrize(
    "user_inputs, expected_seconds",
    [
        pytest.param(["1", "2", "3"], 1 * 3600 + 2 * 60 + 3, id="happy-normal-hms"),
        pytest.param(["0", "0", "0"], 0, id="happy-all-zero"),
        pytest.param(["10", "0", "0"], 10 * 3600, id="happy-only-hours"),
        pytest.param(["0", "45", "0"], 45 * 60, id="happy-only-minutes"),
        pytest.param(["0", "0", "59"], 59, id="happy-only-seconds"),
        pytest.param(["2", "30", "30"], 2 * 3600 + 30 * 60 + 30, id="happy-mixed-values"),
    ],
)
def test_time_in_seconds_happy_paths(countdown_module, monkeypatch, user_inputs, expected_seconds):
    # 
    # Arrange
    inputs_iter = iter(user_inputs)

    def fake_input(prompt=""):
        return next(inputs_iter)

    monkeypatch.setattr(builtins, "input", fake_input)

    # 
    # Act
    result = countdown_module.time_in_seconds()

    # 
    # Assert
    assert result == expected_seconds


@pytest.mark.parametrize(
    "user_inputs, expected_seconds",
    [
        pytest.param(["0", "0", "1"], 1, id="edge-minimal-positive"),
        pytest.param(["0", "59", "59"], 59 * 60 + 59, id="edge-max-minutes-seconds"),
        pytest.param(["23", "59", "59"], 23 * 3600 + 59 * 60 + 59, id="edge-max-typical-daytime"),
        pytest.param(["9999", "0", "0"], 9999 * 3600, id="edge-large-hours"),
    ],
)
def test_time_in_seconds_edge_cases(countdown_module, monkeypatch, user_inputs, expected_seconds):
    # 
    # Arrange
    inputs_iter = iter(user_inputs)

    def fake_input(prompt=""):
        return next(inputs_iter)

    monkeypatch.setattr(builtins, "input", fake_input)

    # 
    # Act
    result = countdown_module.time_in_seconds()

    # 
    # Assert
    assert result == expected_seconds


@pytest.mark.parametrize(
    "user_inputs, expected_exception, msg_substring, test_id",
    [
        pytest.param(
            ["-1", "0", "0"],
            ValueError,
            "negative",
            "error-negative-hours",
            id="error-negative-hours",
        ),
        pytest.param(
            ["0", "-5", "0"],
            ValueError,
            "negative",
            "error-negative-minutes",
            id="error-negative-minutes",
        ),
        pytest.param(
            ["0", "0", "-10"],
            ValueError,
            "negative",
            "error-negative-seconds",
            id="error-negative-seconds",
        ),
        pytest.param(
            ["abc", "0", "0"],
            (ValueError, TypeError),
            None,
            "error-non-numeric-hours",
            id="error-non-numeric-hours",
        ),
        pytest.param(
            ["0", "xyz", "0"],
            (ValueError, TypeError),
            None,
            "error-non-numeric-minutes",
            id="error-non-numeric-minutes",
        ),
        pytest.param(
            ["0", "0", "foo"],
            (ValueError, TypeError),
            None,
            "error-non-numeric-seconds",
            id="error-non-numeric-seconds",
        ),
        pytest.param(
            ["", "0", "0"],
            (ValueError, TypeError),
            None,
            "error-empty-hours-input",
            id="error-empty-hours-input",
        ),
        pytest.param(
            ["0", "", "0"],
            (ValueError, TypeError),
            None,
            "error-empty-minutes-input",
            id="error-empty-minutes-input",
        ),
        pytest.param(
            ["0", "0", ""],
            (ValueError, TypeError),
            None,
            "error-empty-seconds-input",
            id="error-empty-seconds-input",
        ),
    ],
)
def test_time_in_seconds_error_cases(
    countdown_module,
    monkeypatch,
    user_inputs,
    expected_exception,
    msg_substring,
    test_id,  # unused but kept for clarity of parametrization
):
    # 
    # Arrange
    inputs_iter = iter(user_inputs)

    def fake_input(prompt=""):
        return next(inputs_iter)

    monkeypatch.setattr(builtins, "input", fake_input)

    # 
    # Act
    with pytest.raises(expected_exception) as exc_info:
        countdown_module.time_in_seconds()

    # 
    # Assert
    if msg_substring is not None:
        # Only check for a message substring if one is specified
        assert msg_substring.lower() in str(exc_info.value).lower()
