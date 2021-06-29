let counter = 0;

const test = (counter) => {
    if (counter == 5) {
        return "This is a test";
    }
    counter++
    test(counter)
}

test(counter)