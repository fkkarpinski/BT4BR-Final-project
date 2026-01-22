# Interactive game project

## Project Idea
An interactive  application that simulates the scientific publication pipeline for bioinformatics research. Using a simulated dataset based on The Cancer Genome Atlas (TCGA) patterns, it guides a user—playing the role of a researcher—through the steps of a multi-omics analysis: from initial data exploration and testing to visualization and final publication. The game ends in the creation of actual analysis, that can be later viewed.

## Core Features & Principle of Operation
The application is a narrative-driven, single-choice interface structured with a storyline of a researcher in mind.

## Data Description
This project uses a **synthetic dataset** designed to mimic real-world patterns from **The Cancer Genome Atlas Breast Invasive Carcinoma (TCGA-BRCA)** project.

*   **Source Inspiration**: The Cancer Genome Atlas (TCGA) is a landmark project that mapped genomic changes in over 20,000 primary cancers across 33 cancer types. Its data includes genomic sequencing, epigenomics (methylation), transcriptomics (RNA-seq), and proteomics.
    *   Official Portal: [National Cancer Institute Genomic Data Commons (GDC)](https://portal.gdc.cancer.gov/)
    *   Program Info: [TCGA Program Website](https://www.cancer.gov/ccg/research/genome-sequencing/tcga)

*   **Synthetic Data Variables**:
    *   `Patient_ID`: Simulated TCGA patient identifiers (e.g., TCGA-T01 for tumor, TCGA-N01 for normal).
    *   `Sample_Type`: Specifies if the sample is from **Tumor** or adjacent **Normal** tissue.
    *   `Expression`: Log2-normalized gene expression values for **RASSF1**, simulated to be lower in tumors.
    *   `Methylation`: DNA methylation Beta-values (ranging from 0 = unmethylated to 1 = fully methylated) for the RASSF1 promoter region, simulated to be higher in tumors.

*   **Biological Context - The RASSF1 Gene**:
    *   **RASSF1** (Ras Association Domain Family Member 1) is a crucial **tumor suppressor gene**. It is involved in regulating cell cycle progression, apoptosis (programmed cell death), and maintaining genomic stability.
    *   In many cancers, including breast cancer, the **promoter region** of RASSF1 is often **hypermethylated**. This epigenetic modification acts like a "switch" that turns the gene off, silencing its expression and allowing cancer cells to proliferate uncontrollably. This pipeline investigates this exact relationship.

## Installation & Setup
To run this project locally, you need R and the required packages.

1.  **Prerequisites**:
    *   Install [R](https://cran.r-project.org/) (version 4.0+ recommended).
    *   Install [RStudio](https://posit.co/download/rstudio-desktop/) (optional but recommended).

2.  **Install Required R Packages**:
    Run the following commands in your R console:
    ```r
    install.packages(c("dplyr", "ggplot2", "tidyr", "patchwork", "ggpubr", "UpSetR"))
    ```

3.  **Run the Analysis Pipeline**:
    *   Clone this repository or download the `analysis_pipeline.Rmd` (R Markdown) file.
 *   **For reproducibility**: The code includes `set.seed(42)` and `sessionInfo()` to ensure identical results and environment details.

4.  **Run the Interactive Interface (Python)**:
    *   Ensure you have all the dependencies from file requirements.txt
    *   Navigate to the project directory and run: `shiny run app.py`
    *   Open the link from the console

## How to Use the Interactive App
1.  Launch `ui.py`.
2.  Follow the on-screen narrative. You are a scientist preparing a new project.
3.  At each decision point, read the context and choose the option (A or B) that represents the **best practice in reproducible bioinformatics research**.
4.  Your choices lead you to the final, correctly visualized publication pipeline.

## Team Contributions
*   **Franciszek Karpiński**: UI developement, overall logic developement, code developement
*   **Natalia Charzewska**:
*   **Agata Leszczak**: Pipeline developement, Data Visualization & Documentation**. Made the R analysis code, created synthetic data, implemented statistical tests (Wilcoxon, Spearman), and generated all figures (boxplots, heatmap, scatter plot, UpSet plot). Logic developement.

