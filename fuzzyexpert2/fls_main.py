from pyit2fls import IT2FS, trapezoid_mf, tri_mf, IT2FS_Gaussian_UncertMean, \
    IT2FS_plot, IT2FLS, min_t_norm, max_s_norm, TR_plot, crisp
from numpy import linspace


def calculate_FLS(lecture_inp, practic_inp, project_inp, visits_inp):
    severity = linspace(0.0, 10.0, 100)

    # For IT2FS_Gaussian_UncertMean, the parameters define:
    # 1 - The tip of the center point of the curve
    # 2 - The width of the lower curve (higher value = lower width)
    # 3 - The height of the lower curve (higher value = higher tip)
    # 4 - The height of the center point of the outer curve.

    Lecture_low = IT2FS_Gaussian_UncertMean(severity, [0, 2.65, 1, 1.0])
    Lecture_middle = IT2FS_Gaussian_UncertMean(severity, [14, 2.65, 1, 1.0])
    Lecture_high = IT2FS_Gaussian_UncertMean(severity, [20, 2.65, 1, 1.0])

    Practic_low = IT2FS_Gaussian_UncertMean(severity, [0, 2.65, 1, 1.0])
    Practic_middle = IT2FS_Gaussian_UncertMean(severity, [19, 2.65, 1, 1.0])
    Practic_high = IT2FS_Gaussian_UncertMean(severity, [30, 2.65, 1, 1.0])

    Project_low = IT2FS_Gaussian_UncertMean(severity, [0, 2.65, 1, 1.0])
    Project_middle = IT2FS_Gaussian_UncertMean(severity, [28, 2.65, 1, 1.0])
    Project_high = IT2FS_Gaussian_UncertMean(severity, [40, 2.65, 1, 1.0])

    Visits_low = IT2FS_Gaussian_UncertMean(severity, [0, 2.65, 1, 1.0])
    Visits_middle = IT2FS_Gaussian_UncertMean(severity, [7, 2.65, 1, 1.0])
    Visits_high = IT2FS_Gaussian_UncertMean(severity, [10, 2.65, 1, 1.0])

    Score_bad = IT2FS_Gaussian_UncertMean(severity, [2, 1, 1, 1.0])
    Score_med = IT2FS_Gaussian_UncertMean(severity, [3, 1, 1, 1.0])
    Score_good = IT2FS_Gaussian_UncertMean(severity, [4, 1, 1, 1.0])
    Score_excellent = IT2FS_Gaussian_UncertMean(severity, [5, 1, 1, 1.0])

    def plot_lecture_mf():
        IT2FS_plot(Lecture_low, Lecture_middle, Lecture_high,
                   title="Lecture",
                   legends=["Low", "Middle", "High"],
                   )

    def plot_practic_mf():
        IT2FS_plot(Practic_low, Practic_middle, Practic_high,
                   title="Practic",
                   legends=["Low", "Middle", "High"],
                   )

    def plot_project_mf():
        IT2FS_plot(Project_low, Project_middle, Project_high,
                   title="Project",
                   legends=["Low", "Middle", "High"],
                   )

    def plot_visits_mf():
        IT2FS_plot(Visits_low, Visits_middle, Visits_high,
                   title="Visits",
                   legends=["Low", "Middle", "High"],
                   )

    def plot_score_mf():
        IT2FS_plot(Score_bad, Score_med, Score_good, Score_excellent,
                   title="Score",
                   legends=["Bad", "Medium", "Good","Excellent"],
                   )

    myIT2FLS = IT2FLS()

    myIT2FLS.add_input_variable("lecture")
    myIT2FLS.add_input_variable("practic")
    myIT2FLS.add_input_variable("project")
    myIT2FLS.add_input_variable("visits")
    myIT2FLS.add_output_variable("score")

    # Excellent (Оценка 5) - 3 правила
    myIT2FLS.add_rule([("lecture", Lecture_high), ("practic", Practic_high), 
                        ("project", Project_high), ("visits", Visits_high)],
                      [("score", Score_excellent)])
    myIT2FLS.add_rule([("lecture", Lecture_high), ("practic", Practic_high), 
                        ("project", Project_high), ("visits", Visits_middle)],
                      [("score", Score_excellent)])
    myIT2FLS.add_rule([("lecture", Lecture_high), ("practic", Practic_high), 
                        ("project", Project_high), ("visits", Visits_low)],
                      [("score", Score_good)])

    # Good (Оценка 4) - 8 правил
    myIT2FLS.add_rule([("lecture", Lecture_high), ("practic", Practic_middle), 
                        ("project", Project_middle), ("visits", Visits_middle)],
                      [("score", Score_good)])
    myIT2FLS.add_rule([("lecture", Lecture_middle), ("practic", Practic_high), 
                        ("project", Project_middle), ("visits", Visits_middle)],
                      [("score", Score_good)])
    myIT2FLS.add_rule([("lecture", Lecture_middle), ("practic", Practic_middle), 
                        ("project", Project_high), ("visits", Visits_middle)],
                      [("score", Score_good)])
    myIT2FLS.add_rule([("lecture", Lecture_middle), ("practic", Practic_middle), 
                        ("project", Project_middle), ("visits", Visits_high)],
                      [("score", Score_good)])
    myIT2FLS.add_rule([("lecture", Lecture_high), ("practic", Practic_high), 
                        ("project", Project_middle), ("visits", Visits_middle)],
                      [("score", Score_good)])
    myIT2FLS.add_rule([("lecture", Lecture_middle), ("practic", Practic_high), 
                        ("project", Project_high), ("visits", Visits_middle)],
                      [("score", Score_good)])
    myIT2FLS.add_rule([("lecture", Lecture_middle), ("practic", Practic_middle), 
                        ("project", Project_high), ("visits", Visits_high)],
                      [("score", Score_good)])
    myIT2FLS.add_rule([("lecture", Lecture_high), ("practic", Practic_middle), 
                        ("project", Project_middle), ("visits", Visits_high)],
                      [("score", Score_good)])

    # Medium (Оценка 3) - 6 правил
    myIT2FLS.add_rule([("lecture", Lecture_middle), ("practic", Practic_middle), 
                        ("project", Project_middle), ("visits", Visits_low)],
                      [("score", Score_med)])
    myIT2FLS.add_rule([("lecture", Lecture_low), ("practic", Practic_high), 
                        ("project", Project_middle), ("visits", Visits_middle)],
                      [("score", Score_med)])
    myIT2FLS.add_rule([("lecture", Lecture_high), ("practic", Practic_low), 
                        ("project", Project_middle), ("visits", Visits_middle)],
                      [("score", Score_med)])
    myIT2FLS.add_rule([("lecture", Lecture_middle), ("practic", Practic_middle), 
                        ("project", Project_high), ("visits", Visits_low)],
                      [("score", Score_med)])
    myIT2FLS.add_rule([("lecture", Lecture_low), ("practic", Practic_middle), 
                        ("project", Project_middle), ("visits", Visits_high)],
                      [("score", Score_med)])
    myIT2FLS.add_rule([("lecture", Lecture_middle), ("practic", Practic_middle), 
                        ("project", Project_middle), ("visits", Visits_middle)],
                      [("score", Score_med)])

    # Bad (Оценка 2) - 14 правил
    myIT2FLS.add_rule([("lecture", Lecture_middle), ("practic", Practic_low), 
                        ("project", Project_low), ("visits", Visits_low)],
                      [("score", Score_bad)])
    myIT2FLS.add_rule([("lecture", Lecture_low), ("practic", Practic_middle), 
                        ("project", Project_low), ("visits", Visits_low)],
                      [("score", Score_bad)])
    myIT2FLS.add_rule([("lecture", Lecture_low), ("practic", Practic_low), 
                        ("project", Project_middle), ("visits", Visits_low)],
                      [("score", Score_bad)])
    myIT2FLS.add_rule([("lecture", Lecture_low), ("practic", Practic_low), 
                        ("project", Project_low), ("visits", Visits_middle)],
                      [("score", Score_bad)])
    myIT2FLS.add_rule([("lecture", Lecture_low), ("practic", Practic_low), 
                        ("project", Project_low), ("visits", Visits_low)],
                      [("score", Score_bad)])
    myIT2FLS.add_rule([("lecture", Lecture_high), ("practic", Practic_low), 
                        ("project", Project_low), ("visits", Visits_low)],
                      [("score", Score_bad)])
    myIT2FLS.add_rule([("lecture", Lecture_low), ("practic", Practic_high), 
                        ("project", Project_low), ("visits", Visits_low)],
                      [("score", Score_bad)])
    myIT2FLS.add_rule([("lecture", Lecture_low), ("practic", Practic_low), 
                        ("project", Project_high), ("visits", Visits_low)],
                      [("score", Score_bad)])
    myIT2FLS.add_rule([("lecture", Lecture_low), ("practic", Practic_low), 
                        ("project", Project_low), ("visits", Visits_high)],
                      [("score", Score_bad)])
    myIT2FLS.add_rule([("lecture", Lecture_middle), ("practic", Practic_middle), 
                        ("project", Project_low), ("visits", Visits_high)],
                      [("score", Score_bad)])
    myIT2FLS.add_rule([("lecture", Lecture_high), ("practic", Practic_middle), 
                        ("project", Project_middle), ("visits", Visits_low)],
                      [("score", Score_bad)])
    myIT2FLS.add_rule([("lecture", Lecture_middle), ("practic", Practic_middle), 
                        ("project", Project_low), ("visits", Visits_middle)],
                      [("score", Score_bad)])
    myIT2FLS.add_rule([("lecture", Lecture_middle), ("practic", Practic_low), 
                        ("project", Project_middle), ("visits", Visits_middle)],
                      [("score", Score_bad)])
    myIT2FLS.add_rule([("lecture", Lecture_low), ("practic", Practic_middle), 
                        ("project", Project_middle), ("visits", Visits_middle)],
                      [("score", Score_bad)])

    it2out, tr = myIT2FLS.evaluate({"lecture": lecture_inp, "practic": practic_inp, 
                                    "project": project_inp, "visits": visits_inp},
                                   min_t_norm, max_s_norm, severity,
                                   method="Centroid", algorithm="EKM")

    return int((crisp(tr["score"])))