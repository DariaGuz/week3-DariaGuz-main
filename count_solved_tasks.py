#!/usr/bin/env python3
"""
Script to count and display solved tasks from pytest results.
"""
import subprocess
import sys
import re


def run_tests_and_count():
    """Run tests and count passed/failed tasks."""
    try:
        # Run pytest with minimal output
        result = subprocess.run(
            ["python", "-m", "pytest", "tests/", "--tb=no"],
            capture_output=True,
            text=True,
        )

        output = result.stdout + result.stderr

        # Count passed and failed tests
        passed_pattern = r"(\d+) passed"
        failed_pattern = r"(\d+) failed"

        passed_counts = [int(x) for x in re.findall(passed_pattern, output)]
        failed_counts = [int(x) for x in re.findall(failed_pattern, output)]

        passed_count = sum(passed_counts)
        failed_count = sum(failed_counts)

        total_tasks = passed_count + failed_count

        print("📊 РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
        print("=" * 50)
        print(f"✅ Решенные задачи: {passed_count}")
        print(f"❌ Нерешенные задачи: {failed_count}")
        print(
            f"📈 Общий прогресс: {passed_count}/{total_tasks} ({(passed_count/total_tasks*100):.1f}%)"
            if total_tasks > 0
            else "📈 Общий прогресс: 0/0 (0%)"
        )
        print("=" * 50)

        # Grade based on percentage
        if total_tasks > 0:
            percentage = passed_count / total_tasks * 100
            if percentage >= 90:
                grade = "Отлично! 🏆"
            elif percentage >= 75:
                grade = "Хорошо! 👍"
            elif percentage >= 60:
                grade = "Удовлетворительно 📚"
            else:
                grade = "Нужно больше практики 💪"

            print(f"🎯 Оценка: {grade}")

        return passed_count, total_tasks

    except Exception as e:
        print(f"Ошибка при подсчете результатов: {e}")
        return 0, 0


if __name__ == "__main__":
    solved, total = run_tests_and_count()
    sys.exit(0 if solved == total else 1)
