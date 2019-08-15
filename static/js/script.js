$(document).ready(function () {
    // submit button - create new article

    $("#submit-new").on("click", function () {
        // Create new article
        $title = $("#title").val();
        $content = $("#summernote").summernote("code");
        $tags = $("#tags").val();

        if ($title == "" || $content == "" || $tags == "") {
            alert("Please complete all the fields");
        } else {
            $.ajax({
                type: "POST",
                url: "",
                data: {
                    title: $title,
                    content: $content,
                    tags: $tags,
                    is_draft: false,
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
                },
                success: function () {
                    $("#title").val("");
                    $("#summernote").summernote("reset");
                    $("#tags").val("");
                    window.location = "/";
                    alert("Article published.");
                }
            });
        }
    });

    // Save as draft button - save the article as a draft

    $("#save-draft").on("click", function () {
        $title = $("#title").val();
        $content = $("#summernote").summernote("code");
        $tags = $("#tags").val();

        if ($title == "" || $content == "" || $tags == "") {
            alert("Please complete all the fields");
        } else {
            $.ajax({
                type: "POST",
                url: "",
                data: {
                    title: $title,
                    content: $content,
                    tags: $tags,
                    is_draft: true,
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
                },
                success: function () {
                    $("#title").val("");
                    $("#summernote").summernote("reset");
                    $("#tags").val("");
                    window.location = "/";
                    alert("Draft saved.");
                }
            });
        }
    });

    // Summernote for adding content of an artice

    $("#summernote").summernote({
        placeholder: "Start writing your article...",
        tabsize: 2,
        height: 200
    });

    // Click on draft to edit
    //  1. Redirect to new_article view
    //  2. Place values in all the input

    $("#drafts > .card").on('click', function () {
        $title = $(this).find('.card-title').html();
        $content = $(this).find('#content').html();
    });

    $("#previewModal").on('show.bs.modal', function (e) {
        var button = $(e.relatedTarget),
            title = $("#title").val(),
            content = $("#summernote").summernote("code"),
            modal = $(this);
        console.log("############");
        console.log(title);

        modal.find('#ModalTitle').html(title);
        modal.find('.modal-body').html(content);
        // $(".model-tags").html(tags);
    });
});