#!/usr/bin/env python

from core import FTP, File


class Ensembl(FTP):
  """docstring for Ensembl"""
  def __init__(self, username="anonymous", password=""):
    super(Ensembl, self).__init__("ftp.ensembl.org", username, password)

    self.files = {
      # The primary assembly in FASTA format
      "assembly": File("pub/current_fasta/homo_sapiens/dna",
                       "*.dna.primary_assembly.fa.gz"),

      "gtf": File("pub/current_gtf/homo_sapiens/", "*gtf.gz")
    }


class NCBI(FTP):
  """docstring for NCBI"""
  def __init__(self, username="anonymous", password=""):
    # The password is supposed to be your email...
    super(NCBI, self).__init__("ftp.ncbi.nlm.nih.gov", username, password)

    # TODO: refseq? /refseq/

    self.files = {
      # Genbank assembly in FASTA format
      "genbank": File("genbank/genomes/Eukaryotes/vertebrates_mammals/"
                      "Homo_sapiens/GRCh37.p13/Primary_Assembly/"
                      "assembled_chromosomes/FASTA/", "*.fa.gz", 24),

      # All the assembeled chromosomes (+ MT)
      "assembly": File("genomes/Homo_sapiens/Assembled_chromosomes/seq/",
                       "hs_ref_*_chr*.fa.gz", 25),

      # CCDS, manually curated database of transcript annotations
      "ccds": File("pub/CCDS/current_human", "CCDS.current.txt") 
    }

class GATK(FTP):
  """docstring for GATK"""
  def __init__(self, username="gsapubftp-anonymous", password="", version=None,
               assembly="b37"):
    super(GATK, self).__init__("ftp.broadinstitute.org", username, password)

    if version is None:
      # Figure out which is the latest version folder
      folders = [float(folder) for folder in self.ftp.listdir("bundle/")]
      version = max(folders)

    url = "bundle/{dist}/{assembly}".format(dist=folder, assembly=assembly)
    self.files = {
      "1000g": File(url, "1000G_omni*.vcf.gz"),
      "mills": File(url, "Mills_and_1000G_gold_standard.indels.*.vcf.gz"),
      "dbsnp": File(url, "dbsnp_*{}.vcf.gz".format(assembly)),
      "hapmap": File(url, "hapmap_*.vcf.gz"),
      "indels": File(url, "1000G_phase1.indels.*.vcf.gz"),
      "dbsnpex": File(url, "dbsnp_*.excluding_sites_after_*.vcf.gz")
    }

class UCSC(FTP):
  """docstring for UCSC"""
  def __init__(self, username="anonymous", password="yourEmail",
               assembly="hg19"):
    super(UCSC, self).__init__("hgdownload.cse.ucsc.edu", username, password)

    self.files = {
      "assembly": File("goldenPath/currentGenomes/Homo_sapiens/bigZips/",
                       "chromFa.tar.gz")
    }