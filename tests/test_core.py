import unittest

from todo import core


class TestCore(unittest.TestCase):
    def test_add_task(self):
        tasks = []
        task = core.add_task(tasks, "Learn Git")
        self.assertEqual(task["id"], 1)
        self.assertFalse(task["done"])
        self.assertEqual(len(tasks), 1)

    def test_add_empty_title_fails(self):
        with self.assertRaises(ValueError):
            core.add_task([], "   ")

    def test_ids_increase(self):
        tasks = []
        core.add_task(tasks, "A")
        second = core.add_task(tasks, "B")
        self.assertEqual(second["id"], 2)

    def test_complete_task(self):
        tasks = []
        core.add_task(tasks, "A")
        core.complete_task(tasks, 1)
        self.assertTrue(tasks[0]["done"])

    def test_remove_task(self):
        tasks = []
        core.add_task(tasks, "A")
        core.remove_task(tasks, 1)
        self.assertEqual(tasks, [])

    def test_missing_id_raises(self):
        with self.assertRaises(KeyError):
            core.complete_task([], 99)


if __name__ == "__main__":
    unittest.main()
