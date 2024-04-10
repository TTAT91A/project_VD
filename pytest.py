#!/usr/bin/env python3
import sys, requests, argparse
from pydriller import Repository
from datetime import datetime, timezone, timedelta

#Get commit infomation
# def process_commit (repo):
#     print(f"Processing :{repo}")
#     minner=Repository(repo)
#     for commit in minner.traverse_commits():
#         commit_info=CommitInfo(commit)
#         commits_info.append(commit_info)
#     for commit_info in commits_info:   
#         print ("Hash: {}\nauthor: {}\nemail: {}\ndate: {}\nmsg: {}\n------\n".
#                format(commit_info.hash,commit_info.author,commit_info.email,commit_info.date,commit_info.message))

#line of code information        
def extract_nloc(repo):
    print(f"Extracting NLoC from: {repo}")
    total_nloc = 0
    miner = Repository(repo)
    for commit in miner.traverse_commits():
        commit_nloc = sum(mod.nloc for mod in commit.modified_files if mod.nloc is not None)
        print(f"Commit {commit.hash}: NLoC = {commit_nloc}")
        total_nloc += commit_nloc
    print(f"Total NLoC in the repository: {total_nloc}")     

#line changed information
def extract_changed_lines(repo):
    print(f"Extracting changed lines from: {repo}")
    miner = Repository(repo)
    for commit in miner.traverse_commits():
        print(f"Commit {commit.hash}:")
        for mod in commit.modified_files:
            print(f"    Modified file: {mod.filename}")
            # Print added lines
            for line in mod.diff_parsed['added']:
                print(f"                                    added")
                print(f"        + {line[1]}")
                
            # Print deleted lines
            for line in mod.diff_parsed['deleted']:
                print(f"                                    deleted")
                print(f"        - {line[1]}")
                
        print("------\n")  

# def options_onl(repo):
#         user_name = get_user_name(repo) 
#         repo_name = get_repo_name(repo)
    
#         options = {
#         1:lambda: scan_commits(repo),
#         2:lambda: check_T7(repo_name, user_name),
#         } 
            
#         while True:          
#             print("Select an option:")
#             print("1. Scan commit")
#             print("2. Check Pull Request")
#             print("3. End program")
            
#             choice = input("Enter your choice: ")
            
#             if choice.isdigit():
#                 choice = int(choice)
#                 if choice == 3:
#                     print("Ending program.")
#                     break
#                 elif choice in options:
#                     # Get the function corresponding to the choice
#                     chosen_function = options[choice]
#                     # Call the chosen function
#                     chosen_function()
#                 else:
#                     print("Invalid choice. Please select a valid option.")
#             else:
#                 print("Invalid choice. Please select a valid option.")

# def default_case():
#     print("Invalid choice.")
    
def scan_commits(repo, _hash=None, _author=None, _percent=0.0):
    num_commits = 0
    authors_info = check_T3_T5_T6(repo,10,20,30)
    for commit in Repository(repo).traverse_commits():
            num_commits += 1
            percent_rules_violated=0
            commit_hash = commit.hash
            commit_url = f"{repo}/commit/{commit_hash}"
            authored_time = commit.author_date
            authored_by = commit.author.name
            committed_time = commit.committer_date
            committed_by = commit.committer.name
            commit_message = commit.msg
            modified_files = len(commit.modified_files)

            # Lấy thông tin kiểm tra T3 của tác giả
            check_T3_status = authors_info.get(authored_by, {}).get('check_T3', False)
            check_T5_status = authors_info.get(authored_by, {}).get('check_T5', False)
            check_T6_status = authors_info.get(authored_by, {}).get('check_T6', False)

            author_trusted = True

    
            rule1, sensitive_files, total_lines_changed = check_R1(commit)
            rule2_3 = check_R2_R3(commit,repo,0.25)
            rule4 = typical_commit(commit)
            num_rules_checked = 4
            num_rules_violated = 0
            if not author_trusted:
                num_rules_violated += 1
            if not rule1:
                num_rules_violated += 1
            if not rule2_3:
                num_rules_violated += 1
            if not rule4:
                num_rules_violated += 1
            percent_rules_violated = (num_rules_violated / num_rules_checked) * 100

            if _percent is not None:
                if percent_rules_violated < float(_percent):
                    continue

            if _hash and commit_hash != _hash:
                continue
            if _author and authored_by !=_author:
                continue
            
            
            print(f"Commit: {commit_hash}")
            print(f"URL: {commit_url}")
            print(f"Authored on {authored_time} by {authored_by}")
            print(f"Committed on {committed_time} by {committed_by}")
            print(f"Commit Message: {commit_message}")
            print(f"This commit modified {modified_files} files.")   

            if sum([check_T3_status, check_T5_status, check_T6_status]) >= 2:
                print(f"{authored_by} is Trusted")
            else:
                print( f"{authored_by} is Untrusted")
                author_trusted = False
            # In ra phần trăm quy tắc bị vi phạm
            print_sensitive_files(sensitive_files, total_lines_changed)
            print(f"{percent_rules_violated}% of Rules were Violated")
            print()      
            print()

def get_user_name(repo_url):
    repo_url= str(sys.argv[2])
    parts = repo_url.split("/")
    username = parts[3]
    return username

def get_repo_name(repo_url):
    repo_name = repo_url.split('/')[-1].split('.git')[0]
    return repo_name

token = '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'


def check_T2(author_commits_list,author_name, repo_name):
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url=f"https://api.github.com/repos/{author_name}/{repo_name}/contributors", headers=headers)
    if response.status_code == 200:
        contributors = response.json()
        for contributor in contributors:
            login_name = contributor.get('login')
            response = requests.get(url=f"https://api.github.com/users/{login_name}", headers=headers)
            if response.status_code == 200:
                data = response.json()
                created_at = data.get('created_at', '')

                    # Chuyển đổi chuỗi ngày tạo thành đối tượng datetime
                created_at_date = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ')

                # Kiểm tra xem tài khoản có được tạo trong vòng 30 ngày gần đây không
                if created_at_date >= datetime.now() - timedelta(days=30):
                    print(f"Cảnh báo: Tài khoản của tác giả {login_name} đã được tạo trong vòng 30 ngày gần đây.")
                else:
                    print(f"{login_name} is trusted")
            else: 
                print(f"Can not find account {login_name}")
            
from collections import Counter

def check_T3_T5_T6(repo, threshold_T3, threshold_T5, threshold_T6):
    author_commits = get_author_commits(repo)
    violated_authors_T5 = []
    violated_authors_T6 = []

    for author, data in author_commits.items():
        commits = data['commits']
        commit_dates = [commit[1] for commit in commits]
        daily_commits_count = Counter(commit_dates)
        total_commits = len(commits)

        for daily_commits in daily_commits_count.values():
            if daily_commits / total_commits >= threshold_T5 / 100:
                violated_authors_T5.append(author)
                break
        
        if len(commits) < threshold_T3:
            data['check_T3'] = False           
        else:
            data['check_T3'] = True

        # Check T6
        sorted_commits = sorted(commits, key=lambda commit: commit[1])
        for i in range(1, len(sorted_commits)):
            commit_time_diff = sorted_commits[i][1] - sorted_commits[i-1][1]
            if commit_time_diff >= timedelta(days=threshold_T6):
                violated_authors_T6.append(author)
                break
      

    if violated_authors_T5:
        for author in violated_authors_T5:          
            author_commits[author]['check_T5'] = False

    if violated_authors_T6:
        for author in violated_authors_T6:
            author_commits[author]['check_T6'] = False


    return author_commits

 
def check_T7(repo_name, user_name):
    headers = {'Authorization': f'token {token}'}
    response = requests.get(f'https://api.github.com/repos/{user_name}/{repo_name}/pulls?state=closed', headers=headers)

    if response.status_code == 200:
        pulls = response.json()    
        user_pulls = {}
        user_rejected_pulls = {}
        for pull in pulls:
            if 'user' in pull:
                user_login = pull['user']['login']
                if user_login in user_pulls:
                    user_pulls[user_login] += 1
                else:
                    user_pulls[user_login] = 1

                if pull['state'] == 'closed' and pull['merged_at'] is None:
                    if user_login in user_rejected_pulls:
                        user_rejected_pulls[user_login] += 1
                    else:
                        user_rejected_pulls[user_login] = 1
            else:
                print("Pull request is missing user information.")
        
        # In ra tỷ lệ từ chối (T7) của mỗi người dùng
        for user, count in user_pulls.items():
            rejected_pulls = user_rejected_pulls.get(user, 0)
            rejection_rate = (rejected_pulls / count) * 100 if count > 0 else 0
            print(f'User: {user}, Total Pull Requests: {count}, Rejected Pull Requests: {rejected_pulls}, Rejection Rate: {rejection_rate:.2f}%')
    else:
        print(f'Failed to fetch data. Status code: {response.status_code}')

def get_login_name():
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url=f"https://api.github.com/users/{author}", headers=headers)

def get_author_commits(repository):
    author_commits = {}  # A dictionary to hold the author names and their commits
    
    for commit in Repository(repository).traverse_commits():
        author_name = commit.author.name
        commit_time = commit.committer_date  # get commit time
        
        if author_name not in author_commits:
            author_commits[author_name] = {'commits': [], 'check_T3': False, 'check_T5': True, 'check_T6': True}

            
        # Add the commit hash and commit time to the list of this author's commits
        author_commits[author_name]['commits'].append((commit.hash, commit_time,commit.modified_files))
    
    return author_commits

    
#R1
def is_sensitive_file(file_path):
    sensitive_file_extensions = ['.xml', '.json', '.jar', '.ini', '.dat', '.cnf', '.yml', '.toml',
                             '.gradle', '.bin', '.config', '.exe', '.properties', '.cmd', '.build']
    # Kiểm tra xem tập tin có phải là tập tin nhạy cảm không dựa trên phần mở rộng của tên tập tin
    for ext in sensitive_file_extensions:
        if file_path.endswith(ext):
            return True
    return False
#R1 (check sensitive File)
def check_R1(commit):
    sensitive_files = []
    total_lines_changed = 0

    for modified_file in commit.modified_files:
        file_path = modified_file.new_path
        if file_path and is_sensitive_file(file_path):
            sensitive_files.append((file_path, modified_file.added_lines + modified_file.deleted_lines))
            total_lines_changed += modified_file.added_lines + modified_file.deleted_lines
    return not bool(sensitive_files), sensitive_files, total_lines_changed

def print_sensitive_files(sensitive_files, total_lines_changed):
    if sensitive_files:
        print(f"The commit changed {len(sensitive_files)} potentially 'sensitive' files:")
        if total_lines_changed == 0:
            print("No lines changed in sensitive files.")
        else:
            for file_path, lines_changed in sensitive_files:
                proportion = lines_changed / total_lines_changed * 100
                print(f"{file_path} - MODIFY - commit proportion: {proportion:.2f}%")
    else:
        print("The commit did not change any potentially 'sensitive' files.")


#R2,3
contributor_files_cache = {}

def check_R2_R3(commit, repo,threshold):
    contributor = commit.author.name
    touched_files = commit.modified_files
    touched_file_count = len(touched_files)

    # Kiểm tra xem danh sách đã được lưu trữ trong cache chưa
    if contributor in contributor_files_cache:
        contributor_files = contributor_files_cache[contributor]
    else:
        # Nếu chưa, lấy danh sách các tệp đã thay đổi bằng cách duyệt qua các commit
        contributor_files = set()
        for commit in Repository(repo).traverse_commits():
            if commit.author.name == contributor:
                for modification in commit.modified_files:
                    contributor_files.add(modification.filename)
        # Lưu trữ danh sách vào cache để sử dụng cho các lần kiểm tra sau
        contributor_files_cache[contributor] = contributor_files

    contributor_file_count = len(contributor_files)
    threshold_count = int(contributor_file_count * threshold)

    if touched_file_count > threshold_count:
        return False
    else:
        return True

def calculate_hunks(modified_files):
    total_hunks = 0
    for modified_file in modified_files:
        # Số dòng mã mới
        new_loc = modified_file.added_lines
        # Số dòng mã cũ
        old_loc = modified_file.deleted_lines

        # Tính delta
        delta = new_loc - old_loc

        # Ngưỡng để xác định số lượng hunks (ví dụ: 10)
        threshold = 10

        # Tính số lượng hunks
        hunks = delta // threshold
        total_hunks += hunks

    return total_hunks

#R4 
def typical_commit(commit):
        files = commit.files
        lines = commit.lines
        hunks = calculate_hunks(commit.modified_files)
        if (files >= 2 and files <= 4) or (lines <= 50 or hunks <=8):          
                return True
        else:
            return False
      



def main():
    parser = argparse.ArgumentParser(description=' App Description')

    # Add your command-line options here
    # For example:
    # parser.add_argument('--input', help='Input file path')
    # parser.add_argument('--output', help='Output file path')
    parser.add_argument('-path',help='path to repo')
    parser.add_argument('-nloc', action='store_true', help='Extract number of lines of code (NLoC)')
    parser.add_argument('-changes', action='store_true', help='Extract changed lines of code')
    parser.add_argument('-onl',help='Input file url')
    parser.add_argument('-hash', help='Giới hạn đầu ra cho commit cụ thể')
    parser.add_argument('-author',help='author name')

    parser.add_argument('-percent',help='violated rate')
    args = parser.parse_args()
    # Your application logic goes here
    # For example:
    # if args.input:
    #     process_input(args.input)
    # if args.output:
    #     save_output(args.output)
    
    if args.nloc:
        extract_nloc(args.onl)
    if args.changes:
        extract_changed_lines(args.onl)      
    if args.onl:
        scan_commits(args.onl,args.hash,args.author,args.percent)
        
if __name__ == "__main__":
    main()