from time import time_ns


class Runner:
    nanos_to_sec = (10 ** -9)

    def __init__(self, frequency, verbosity):
        self.runner_stats_dict = {}
        self.runner_frequency = 1 / frequency  # Input received in hertz
        self.verbosity = verbosity  # 0 for no console output, 1 for console output
        print("Runner Initialized")

    def __del__(self):
        print("terminating runner")

    def display_runner_stats_dict(self):
        print(f"{self.runner_stats_dict}")

    def display_high_precision_runner_data(self, current_time, start_time_sec, end_time_sec, next_iter_time):
        print(f"Start time: {current_time - start_time_sec} \
| End time: {end_time_sec - start_time_sec} \
| Next Iter starting at: {next_iter_time - start_time_sec} \
| Sleeping for {next_iter_time - end_time_sec} \
| Percentage of interval used: \
{Runner.check_workframe_percentage(self, current_time, start_time_sec, end_time_sec)}%")

    def check_workframe_percentage(self, current_time, start_time_sec, end_time_sec):
        return (100 * ((end_time_sec - start_time_sec) - (current_time - start_time_sec)) / self.runner_frequency)

    def resume_at(self, next_iter_time):
        # We cannot use the time.sleep function because it is very slow and innacurate
        # By doing it this way, we can achieve a 0.0001 second accuracy (vs the 0.16 second time.sleep accuracy)
        while (True):
            # Check current time
            current_time_sec = time_ns() * Runner.nanos_to_sec
            if current_time_sec > next_iter_time:
                break

    def run_simulation_loop(self):
        start_time_sec = time_ns() * Runner.nanos_to_sec
        next_iter_time = start_time_sec + self.runner_frequency
        self.runner_stats_dict["runner_heartbeat"] = 0
        while (True):
            # Start runner loop
            if self.runner_stats_dict["runner_heartbeat"] % 100 == 0:
                Runner.display_runner_stats_dict(self)

            current_time = time_ns() * Runner.nanos_to_sec
            self.runner_stats_dict["runner_heartbeat"] += 1
            self.runner_stats_dict["running_time"] = next_iter_time - \
                start_time_sec

            # ============== Start Runner Work ===============
            # Perform Tasks here

            # ============== Stop Runner Work ================
            end_time_sec = time_ns() * Runner.nanos_to_sec
            self.runner_stats_dict["last_loop_work_time"] = end_time_sec - current_time

            if Runner.check_workframe_percentage(self, current_time, start_time_sec, end_time_sec) > 100.0:
                print("Overrun Detected!")

            if self.verbosity > 0:
                Runner.display_high_precision_runner_data(
                    self, current_time, start_time_sec, end_time_sec, next_iter_time)
            Runner.resume_at(self, next_iter_time)
            next_iter_time += self.runner_frequency
            # End runner loop


real_time_runner = Runner(1, 1)

real_time_runner.run_simulation_loop()
