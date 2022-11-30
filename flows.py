# def pipe_outputs(num_pipes, steps):

#     flows = {}

#     for i in range(num_pipes):
#         flows[i] = 8

#     for i in steps:
#         if len(i) == 2:
#             flows[i[0] + 1] = flows[i[0]]
#             flows[i[0] - 1] = i[1]
#             flows[i[0]] = i[1]
#             # break
#         if len(i) == 1:
#             flows[i[0] - 1] = flows[i[0]] + flows[i[0] - 1]
#             flows.pop(i[0])
#             # print(i[0])
#             # print(i[0] - 1)
#             # print('flows[i[0]]', flows[i[0]])
#             # print('flows[i[0] - 1]', flows[i[0] - 1])
#             # print(flows)
#             # break

#     return list(flows.values())
#     # return []

def pipe_outputs(num_pipes, steps):
    flow = [8] * num_pipes
    for step in steps:
        if len(step) == 1:
            flow[step[0] - 1] += flow.pop(step[0])
        elif len(step) == 2:
            flow.insert(step[0] - 1, step[1])
            flow[step[0]] -= step[1]
    return flow

def pipe_outputs(num_pipes, steps):
    pipes_flow = [8] * num_pipes
    for step in steps:
        if len(step) == 2:
            curr_pipe = step[0] - 1
            pipe_left = [step[1]]
            pipe_right = [pipes_flow[curr_pipe] - step[1]]
            pipes_flow = pipes_flow[:curr_pipe] + pipe_left + pipe_right + pipes_flow[curr_pipe+1:]
        else:
            curr_pipe = step[0] - 1
            new_flow_amount = pipes_flow[curr_pipe] + pipes_flow[curr_pipe+1]
            pipes_flow[curr_pipe] = new_flow_amount
            pipes_flow.pop(curr_pipe+1)
    return pipes_flow


num_pipes = 3
steps = [[1], [1], [1, 2]]
# steps = [[2, 4], [1], [1], [1, 2]]

print(pipe_outputs(num_pipes,steps))
